package com.jh.jwt.controller;

import com.jh.jwt.service.UserService;
import lombok.Builder;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.apache.tomcat.util.http.parser.Authorization;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;

@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PostMapping("/login")
    public ResponseEntity<LoginResponseDto> login(@RequestBody LoginRequestDto dto) {
        return ResponseEntity.ok().body(userService.login(dto.getUsername(), dto.getPassword()));
    }

    @PostMapping("/sign")
    public Long sign(@RequestBody RequestSignupDto dto) {
        return ResponseEntity.ok().body(userService.join(dto.getUsername(), dto.getPassword(), dto.getAuth())).getBody();
    }

    @PostMapping("/refresh")
    public ResponseEntity<LoginResponseDto> refresh(HttpServletRequest request) {
        return ResponseEntity.ok().body(userService.refresh(request));
    }

    @PostMapping("/logout")
    public ResponseEntity<String> logout(HttpServletRequest request) {
        return ResponseEntity.ok().body(userService.logout(request));
    }

    @Data
    public static class RefreshTokenRequestDto {
        private String token;
    }

    @Data
    public static class LoginRequestDto {
        private String username;
        private String password;
    }

    @Data
    public static class RequestSignupDto {
        String username;
        String password;
        String auth;
    }
}
