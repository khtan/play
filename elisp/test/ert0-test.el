;; * comments
;; The invocation has interaction with the shell
;;  | kwee1-ubuntu | emacs shell works
;;  | air          | emacs shell does not work
;;  | air          | git bash shell works
;;    emacs -batch -l ert -l ert0.el -eval '(ert-run-tests-batch-and-exit "t3")'
;; But switching " and ' also does not work
;; This may have permanent side effects
;; stdbuf -i0 -o0 -e0 emacs -batch -l ert -l ert0.el -f ert-run-tests-batch-and-exit
(require 'ert)
;; ** utility print-two-variables
(defun print-two-variables (var1 var2)
  "Print two variables with different output functions"
  (print "-- print")
  (print var1)
  (print var2)
  (print "-- prin1")
  (prin1 var1)
  (prin1 var2)
  (print "----- princ")
  (princ var1)
  (princ var2)
  (print "----- pp")
  (pp var1)
  (pp var2)
  (print "----- message")
  ;; put this last to flush, bec pp does not seem to flush
  (message "message: %s - %s" var1 var2)
)
;; ** tests
;; need something here
;; ** ch01
;; *** t0-how-to-print-string
(ert-deftest t0-how-to-print-string()
  (let ((msg "t0-how-to-print-string")(msg2 "hello world"))
    (print-two-variables msg msg2)
  )
)
;; *** t1-how-to-print-list
(ert-deftest t1-how-to-print-list()
  (let ((msg '(rose violet daisy buttercup))(msg2 "world"))
    (print-two-variables msg msg2)
))
;; *** t2-how-to-print-boolean
(ert-deftest t2-how-to-print-boolean()
  "Printing t and nil"
  (let ((msg t)(msg2 nil))
    (print-two-variables msg msg2)
))
;; *** t3-how-to-print-boolean
(ert-deftest t3-how-to-print-boolean()
"Printing expressions turning t and f"
  (let ((msg (= 1 1))(msg2 (= 1 2)))
    (print-two-variables msg msg2)
))
;; *** t4-how-to-print-variable-value
(ert-deftest t4-how-to-print-variable-value()
"Printing a variable fill-column's value"
  (let ((msg fill-column))
     (print msg)
  )
)
;; *** variables
;; The author shows how errors are manifested in emacs with a void-function and void-variable case
;; For ert, we can either use the expected-result or should-error
;;   should-error is preferred because the error string can be checked
;; *** x1.7-void-function-expected-fail
(ert-deftest x1.7-expected-fail-void-function()
  "Should not be able to treat fill-column variable as a function"
  :expected-result :failed
  (let ((msg (fill-column)))
    (print msg)
    (message ">%s<" msg)
  )
)
;; *** x1.7-void-function-expected-fail
(ert-deftest x1.7-should-error-void-function()
  "Should not be able to treat fill-column variable as a function"
  (let
    (
      (msg (should-error(fill-column) :type 'void-function))
    )
    (print msg)
    (message ">%s< %s" msg (listp msg))
  );; let
);; ert-deftest
;; *** x1.7-void-variable
(ert-deftest x1.8a-void-variable()
  "Should not be able to treat + as a variable"
  (should-error (+) :type 'void-variable) 
)
(ert-deftest x1.8-void-variable()
  "Should not be able to treat + as a variable"
  :expected-result :failed
  (let ((msg +))
    (print msg)
    (message ">%s<" msg)
  )
)
;; *** how to print errors
(ert-deftest t5-should-error()
  "How to use should-error"
  (let ((msg (should-error (/ 1 0))))
    (print msg)
    (message ">%s<" msg)
    )
)

