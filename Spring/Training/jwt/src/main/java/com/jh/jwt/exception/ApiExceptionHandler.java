package com.jh.jwt.exception;

import lombok.Data;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class ApiExceptionHandler {

    @ExceptionHandler(UsernameNotFoundException.class)
    public ResponseEntity<Object> usernameNotFoundExceptionHandler(UsernameNotFoundException e) {
        ErrorResponse errorResponse = new ErrorResponse("error", 404, e.getMessage());
        return ResponseEntity.badRequest().body(errorResponse);
    }

    @ExceptionHandler(BadCredentialsException.class)
    public ResponseEntity<Object> badCredentialsExceptionHandler(BadCredentialsException e) {
        ErrorResponse errorResponse = new ErrorResponse("error", 400, e.getMessage());
        return ResponseEntity.badRequest().body(errorResponse);
    }

    @ExceptionHandler(NotLoggedInException.class)
    public ResponseEntity<Object> NotLoggedInExceptionHandler(NotLoggedInException e) {
        ErrorResponse errorResponse = new ErrorResponse("error", 400, e.getMessage());
        return ResponseEntity.badRequest().body(errorResponse);
    }

    @Data
    public static class ErrorResponse {
        private final String status;
        private final Integer code;
        private final String message;
    }
}
