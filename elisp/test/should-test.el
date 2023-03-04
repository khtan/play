;; * intent
;; show how to use the should macro
;; * tests
;;
(ert-deftest a1-should-equal-number()
  (should(= 2 2))
)
(ert-deftest a2-should-fail-equal-number()
  :expected-result :failed
  (should(= 2 3))
)
(ert-deftest a3-should-not-equal-number()
  (should-not(= 2 3))
)
(ert-deftest b1-should-equal-string()
  (should(string= "hello" "hello"))
)
(ert-deftest b2-should-fail-equal()
  :expected-result :failed
  (should(string= "hello" "world"))
)
(ert-deftest b3-should-not-equal()
  (should-not(string= "hello" "world"))
)
(ert-deftest c1-should-equal-list()
  (should(equal '(a b c) '(a b c)))
)
(ert-deftest c2-should-fail-equal-list()
  :expected-result :failed
  (should(equal '(a b c) '(c b a)))
)
(ert-deftest c3-should-not-equal-list()
  (should-not(equal '(a b c) '(c b a)))
)

(ert-deftest d0-type-of-list()
  (let ((lA '(a b c)))
    (message "type-of lA = %s" (type-of lA))
    (message "type-of '(a b c) = %s" (type-of '(a b c)))
  )

)
;; list= exists but what does it do?
(ert-deftest t10-should-=-list()
  (should(list= '(a b c) '(a b c)))
)

