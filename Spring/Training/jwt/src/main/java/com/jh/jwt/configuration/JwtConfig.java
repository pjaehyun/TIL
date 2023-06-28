package com.jh.jwt.configuration;

import com.jh.jwt.utils.RedisUtil;
import com.jh.jwt.utils.TokenProvider;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// TokenProvider에 의존성을 주입하고 빈을 생성하는 설정 파일
@Configuration
@RequiredArgsConstructor
public class JwtConfig {

    @Value("${jwt.secret}")
    private String secret;

    @Value("${jwt.access_token_expired}")
    private Long accessTokenExpired;

    @Value("${jwt.refresh_secret}")
    private String refreshSecret;

    @Value("${jwt.refresh_token_expired}")
    private Long refreshTokenExpired;

    private final RedisUtil redisUtil;

    @Bean(name = "tokenProvider")
    public TokenProvider tokenProvider() {
        return new TokenProvider(secret, accessTokenExpired, refreshSecret, refreshTokenExpired, redisUtil);
    }
}
