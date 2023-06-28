package com.jh.jwt.utils;

import com.jh.jwt.domain.CustomUserDetails;
import com.jh.jwt.exception.NotLoggedInException;
import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.security.SignatureException;
import org.springframework.http.HttpHeaders;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.util.StringUtils;

import javax.servlet.http.HttpServletRequest;
import java.security.Key;
import java.util.*;
import java.util.stream.Collectors;

public class TokenProvider {

    protected final String secret;
    protected final String refreshSecret;

    protected final long accessTokenExpired;
    protected final long refreshTokenExpired;

    private final RedisUtil redisUtil;

    protected Key accessKey;
    protected Key refreshKey;
    public TokenProvider(String secret, Long expiredMs, String refreshSecret, Long refreshTokenExpired, RedisUtil redisUtil){
        this.secret = secret;
        this.accessTokenExpired = expiredMs;
        this.refreshSecret = refreshSecret;
        this.refreshTokenExpired = refreshTokenExpired;

        byte[] accessKeyBytes = Base64.getDecoder().decode(secret);
        this.accessKey = Keys.hmacShaKeyFor(accessKeyBytes);

        byte[] refreshKeyBytes = Base64.getDecoder().decode(refreshSecret);
        this.refreshKey = Keys.hmacShaKeyFor(refreshKeyBytes);

        this.redisUtil = redisUtil;
    }

    public String getUsername(String token) {
        return Jwts.parserBuilder().setSigningKey(accessKey).build().parseClaimsJws(token).getBody().get("username", String.class);
    }

    public String getRefreshUsername(String token) {
        return Jwts.parserBuilder().setSigningKey(refreshKey).build().parseClaimsJws(token).getBody().get("username", String.class);
    }

    public Collection<? extends GrantedAuthority> getAuthority(String token) {
        Claims claims = Jwts.parserBuilder().setSigningKey(accessKey).build().parseClaimsJws(token).getBody();
        return Arrays.stream(claims.get("auth").toString().split(","))
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
    }

    // 토큰 생성
    public String createAccessJwt(CustomUserDetails principal) {
        Claims claims = Jwts.claims();
        claims.put("username", principal.getUsername());
        claims.put("auth", principal.getAuthorities());

        return  Jwts.builder()
                .setClaims(claims)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + accessTokenExpired))
                .signWith(accessKey, SignatureAlgorithm.HS512)
                .compact();
    }

    public String createRefreshJwt(CustomUserDetails principal) {
        Claims claims = Jwts.claims();
        claims.put("username", principal.getUsername());

        return  Jwts.builder()
                .setClaims(claims)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + refreshTokenExpired))
                .signWith(refreshKey, SignatureAlgorithm.HS512)
                .compact();
    }

    public String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader(HttpHeaders.AUTHORIZATION);
        if (StringUtils.hasText(bearerToken) && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }

    public boolean validateToken(String token) {
        try {
            Claims claims = Jwts.parserBuilder().setSigningKey(accessKey).build().parseClaimsJws(token).getBody();
            if (redisUtil.hasKeyBlackList(token)) {
                throw new SignatureException("로그인을 해주세요.");
            }
            return true;
        } catch(MalformedJwtException | SignatureException e) {
            throw new MalformedJwtException("잘못된 JWT 서명입니다.");
        } catch(ExpiredJwtException e) {
            throw new ExpiredJwtException(e.getHeader(), e.getClaims(), "만료된 JWT 토큰입니다.");
        } catch(UnsupportedJwtException e) {
            throw new UnsupportedJwtException("지원하지 않는 JWT 토큰입니다.");
        } catch(IllegalArgumentException e) {
            throw new IllegalArgumentException("JWT 토큰이 잘못되었습니다.");
        }
    }

    public boolean validateRefreshToken(String token) {
        try {
            Claims claims = Jwts.parserBuilder().setSigningKey(refreshKey).build().parseClaimsJws(token).getBody();
            return true;
        } catch(MalformedJwtException | SignatureException  |  ExpiredJwtException |  UnsupportedJwtException | IllegalArgumentException e) {
            System.out.println("e = " + e);
            throw new NotLoggedInException("로그인을 해주세요.");
        }
    }

}
