;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname catagorize-frame) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Image -> String
;; Categorize a frame based on area and proportions.
(check-expect (categorize-frame (rectangle 100 101 "solid" "red")) "massive")
(check-expect (categorize-frame (rectangle 10 30 "solid" "red")) "tall-strip")
(check-expect (categorize-frame (rectangle 50 10 "solid" "red")) "wide-strip")
(check-expect (categorize-frame (rectangle 20 20 "solid" "red")) "perfect-square")
(check-expect (categorize-frame (rectangle 20 30 "solid" "red")) "standard")

;(define (categorize-frame img)
 ; (if ... ; start your first 'if' here
 ;     ...
 ;     (if ... ; start your next nested 'if' here
 ;         ...
  ;        ...)))

(define (categorize-frame img)
  (cond [(>(* (image-height img) (image-width img)) 10000) "massive"]
         [(> (image-height img) (* 2 (image-width img))) "tall-strip"]
         [(> (image-width img) (* 2 (image-height img))) "wide-strip"]
         [(= (image-height img) (image-width img)) "perfect-square"]
         [else "standard"]
        )

  )