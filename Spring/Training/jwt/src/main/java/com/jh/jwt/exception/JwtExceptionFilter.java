package com.jh.jwt.exception;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.jsonwebtoken.*;
import io.jsonwebtoken.security.SignatureException;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Component
@Slf4j
public class JwtExceptionFilter extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        try {
            filterChain.doFilter(request, response);
        } catch (MalformedJwtException e){
            log.error("JWT Filter MalformedJwtException Exception");
            setErrorResponse(response, HttpStatus.UNAUTHORIZED, e);
        } catch (ExpiredJwtException e) {
            log.error("JWT Filter ExpiredJwtException Exception");
            setErrorResponse(response, HttpStatus.UNAUTHORIZED, e);
        } catch (UnsupportedJwtException e) {
            log.error("JWT Filter UnsupportedJwtException Exception");
            setErrorResponse(response, HttpStatus.UNAUTHORIZED, e);
        } catch (SignatureException e) {
            log.error("JWT Filter SignatureException Exception");
            setErrorResponse(response, HttpStatus.UNAUTHORIZED, e);
        } catch (IllegalArgumentException e) {
            log.error("JWT Filter IllegalArgumentException Exception");
            setErrorResponse(response, HttpStatus.UNAUTHORIZED, e);
        }
    }

    public void setErrorResponse(HttpServletResponse response, HttpStatus status, Throwable e) {
        ObjectMapper objectMapper = new ObjectMapper();
        response.setStatus(status.value());
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        ErrorResponse errorResponse = new ErrorResponse("error",status, e.getMessage());
        try {
            response.getWriter().write(objectMapper.writeValueAsString(errorResponse));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    @Data
    public static class ErrorResponse {
        private final String status;
        private final HttpStatus code;
        private final String message;
    }
}
