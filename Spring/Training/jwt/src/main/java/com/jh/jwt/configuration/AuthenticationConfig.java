package com.jh.jwt.configuration;

import com.jh.jwt.exception.JwtExceptionFilter;
import com.jh.jwt.utils.TokenProvider;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class AuthenticationConfig {

    private final TokenProvider tokenProvider;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity httpSecurity) throws Exception {
        return httpSecurity
                // JWT를 사용하기 때문에 httpBasic, csrf를 disable
                .httpBasic().disable()
                .csrf().disable()
                .cors().and()
                .authorizeRequests()
                // 경로 설정
                .antMatchers("/api/v1/users/login").permitAll()
                .antMatchers("/api/v1/users/sign").permitAll()
                .antMatchers(HttpMethod.POST, "/api/v1/reviews").authenticated()
                .and()
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                .and()
                // 필터를 거치기 이전에 JwtFilter를 먼저 거치도록 설정
                .addFilterBefore(new JwtFilter(tokenProvider), UsernamePasswordAuthenticationFilter.class)
                // Jwt 필터를 거치기 전에 Exception 관리를 위해 JwtException Filter를 등록
                .addFilterBefore(new JwtExceptionFilter(), JwtFilter.class)
                .build();
    }
}
