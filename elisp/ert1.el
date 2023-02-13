(defun myfunc (x)
  (let ((a 2))
  (* a x)))

(myfunc 7)
;;(progn
;;  (equal (myfunc 7) 14))

(require 'ert)
(ert-deftest t1-myfunc-test ()
  "t1 test myfunc"
  (should (equal (myfunc 7) 14)))

(ert-deftest t2-myfunc-test ()
  "t2 test myfunc"
  (should (equal (myfunc 10) 20)))
