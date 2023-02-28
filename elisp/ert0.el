;; The invocation has interaction with the shell 
;;  | kwee1-ubuntu | emacs shell works
;;  | air          | emacs shell does not work
;;  | air          | git bash shell works
;;    emacs -batch -l ert -l ert0.el -eval '(ert-run-tests-batch-and-exit "t3")'
;; But switching " and ' also does not work
;; This may have permanent side effects
;; stdbuf -i0 -o0 -e0 emacs -batch -l ert -l ert0.el -f ert-run-tests-batch-and-exit
(require 'ert)
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
(ert-deftest t0-how-to-print-string()
  (let ((msg "t0-how-to-print-string")(msg2 "hello world"))
    (print-two-variables msg msg2)
  )
)


(ert-deftest t1-how-to-print-list()
  (let ((msg '(rose violet daisy buttercup))(msg2 "world"))
    (print-two-variables msg msg2)
))

(ert-deftest t2-how-to-print-boolean()
  (let ((msg t)(msg2 nil))
    (print-two-variables msg msg2)
))

(ert-deftest t3-how-to-print-boolean()
  (let ((msg (= 1 1))(msg2 (= 1 2)))
    (print-two-variables msg msg2)
))
