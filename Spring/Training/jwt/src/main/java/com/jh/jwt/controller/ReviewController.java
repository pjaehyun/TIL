package com.jh.jwt.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/reviews")
@RequiredArgsConstructor
public class ReviewController {

    @PostMapping
    public ResponseEntity<String> writeReview(Authentication authentication) {
        System.out.println("authentication = " + authentication);
//        System.out.println("authentication.getAuthorities() = " + authentication.getAuthorities());
        return ResponseEntity.ok().body(authentication.getName() + "님의 리뷰 등록이 완료 되었습니다.");
    }
}
