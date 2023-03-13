(defun type-of-animal (characteristic)
  "Print message in echo area depends on CHARACTERISTICS.
If the CHARACTERISTICS is the string \"fierce\",
then warn of a tiger"
  (if (equal characteristic "fierce")
      (message "It is a tiger")
    (message "It is not fierce!")))

(defun append-to-buffer (buffer start end)
  "Append to specified buffer the text of the region.
     It is inserted into that buffer before its point.

     When calling from a program, give three arguments:
     BUFFER (or buffer name), START and END.
     START and END specify the portion of the current buffer to be copied."
  (interactive
   (list (read-buffer "Append to buffer: " (other-buffer
                                            (current-buffer) t))
         (region-beginning) (region-end)))
  (let ((oldbuf (current-buffer)))
    (save-excursion
      (let* ((append-to (get-buffer-create buffer))
             (windows (get-buffer-window-list append-to t t))
             point)
        (set-buffer append-to)
        (setq point (point))
        (barf-if-buffer-read-only)
        (insert-buffer-substring oldbuf start end)
        (dolist (window windows)
          (when (= (window-point window) point)
            (set-window-point window (point))))))))

(defun fill-column-check(size)
  "Is fill-column greater than SIZE?"
  (if (> fill-column size)
      (message "fill-column exceeds %d" size)
      (message "fill-column less than %d" size)
  )
)
; tests
(fill-column-check 20)
(fill-column-check 100)

