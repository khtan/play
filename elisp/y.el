(get-buffer "y.el")
(get-buffer "z.el")
(if (bufferp (get-buffer "y.el")
   (message "ok")
   (message "nok")
   )
)

(buffer-name)
(+ 3 4)

(if (> 5 4)
  (message "5 is greater than 4!")
  (message "5 is less than 4!")
)
(if (bufferp (get-buffer "y.el"))
    (message "5 is greater than 4!")
  (message "5 is less than 4!")
)


(defun check-buffer-exists (bname)
  "Prints whether buffer exists or not"
  (if (bufferp (get-buffer bname) )
      (message "%s exists" bname)
      (message "%s does not exists" bname)
  )
)

(check-buffer-exists "y.el")
(check-buffer-exists "z.el")

(defun simplified-end-of-buffer ()
  "Move point to the beginning of the buffer;
     leave mark at previous position."
  (interactive)
  (push-mark)
  (goto-char (point-max)))

(defun check-buffer-exists (bname)
  "Prints whether buffer exists or not"
  (interactive
    (list
      (read-buffer "Buffer name: "
        (other-buffer (current-buffer) t)
      )
    )
  )
  (if (get-buffer bname)
    (message "%s exists" bname)
    (message "%s does not exists" bname)
  )
)

(if (> (buffer-size) 10000)
    ;; Avoid overflow for large buffer sizes!
  (* (prefix-numeric-value arg) (/ size 10)
  )
  (/
   (+ 10 (* size (prefix-numeric-value arg))
   )
   10
  )
)

(defun test-number (num1 num2)
  (if(> num1 num2)
    (message "%d is greater than %d" num1 num2)
    (if(< num1 num2)
      (message "%d is less than %d" num1 num2)
      (message "%d is equal to %d" num1 num2)
    )
  )
)

(test-number 2 5)
(test-number 5 2)
(test-number 2 2)

(let (c 56))

(defun multiply-pair (num1 num2)
  "Multiply num1 by num2."
  (* num1 num2))

(multiply-pair 3 7)
