;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname tst) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;image, image -> boolean
; the function takes the image and return true if the first image is larger than the second

(check-expect (larger-img? (circle 20 "solid" "blue") (square 20 "solid" "red")) true)
(check-expect (larger-img? (rectangle 10 20 "solid" "blue") (rectangle 20 10 "solid" "red")) false)
(check-expect (larger-img? (ellipse 60 30 "outline" "blue") (square 20 "solid" "red")) true)


;(define (larger-img? img1 img2) false) ;stub
;(define (larger-img? img1 img2)
;(...img1 img2)
;) templete

(define (larger-img? img1 img2)
  (and(> (image-width img1) (image-width img2)) 
      (> (image-height img1) (image-height img2))))



  