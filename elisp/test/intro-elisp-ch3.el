;; * comments
;;    emacs -batch -l ert -l intro-elisp-ch3.el -eval '(ert-run-tests-batch-and-exit "t3-1")'
;; * useful functions
(defun multiply-by-seven (number)
  "Multiply NUMBER by seven"
  (* 7 number)
)
(defun multiply-by-sevenB (number)
  "Multiply NUMBER by seven"
  (+ number number number number number number number)
)
(defun multiply-by-seven-interactive (number)
  "Multiply NUMBER by seven"
  (interactive "p")
  (message "Result is %d" (* 7 number)
  (multiply-by-seven number)
  )
;; * tests
;; ** 3.1 defun macro
(ert-deftest t3-1-multiply-by-seven ()
   "Test for multiply-by-seven"
   (should(= (multiply-by-seven 3) 21))
)
(ert-deftest t3-2-multiply-by-sevenB ()
  "Test for multiply-by-seven"
  (should(= (multiply-by-seven 3) (multiply-by-sevenB 3)))
)
