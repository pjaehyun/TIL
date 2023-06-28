package com.jh.jwt.configuration;

import com.jh.jwt.utils.TokenProvider;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpHeaders;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.util.StringUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.*;

// 토큰 인증 계층
@RequiredArgsConstructor
public class JwtFilter extends OncePerRequestFilter {
    protected final Logger logger = LoggerFactory.getLogger(JwtFilter.class);
    private final TokenProvider tokenProvider;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        if(request.getServletPath().startsWith("/api/v1/users/login") || request.getServletPath().startsWith("/api/v1/users/sign") || request.getServletPath().startsWith("/api/v1/users/refresh")){
            filterChain.doFilter(request, response);
        } else {
            String token = tokenProvider.resolveToken(request);
            if (tokenProvider.validateToken(token)){
                System.out.println("token = " + token);
                // Username, Authorities Token에서 꺼내기
                String username = tokenProvider.getUsername(token);
                Collection<? extends GrantedAuthority>  authority = tokenProvider.getAuthority(token);
                logger.info("username: {}", username);
                logger.info("authority: {}", authority);

                // 권한 부여
                UsernamePasswordAuthenticationToken authenticationToken =
                        new UsernamePasswordAuthenticationToken(username, null, authority);
                // Detail을 넣어준다.
                authenticationToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authenticationToken);
                filterChain.doFilter(request, response);
            }
        }
    }
}
