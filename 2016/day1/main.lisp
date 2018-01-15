
(defparameter *input* '((L 3) (R 1) (L 4) (L 1) (L 2) (R 4) (L 3) (L 3) (R 2) (R 3) (L 5) (R 1) (R 3) (L 4) (L 1) (L 2) (R 2) (R 1) (L 4) (L 4) (R 2) (L 5) (R 3) (R 2) (R 1) (L 1) (L 2) (R 2) (R 2) (L 1) (L 1) (R 2) (R 1) (L 3) (L 5) (R 4) (L 3) (R 3) (R 3) (L 5) (L 190) (L 4) (R 4) (R 51) (L 4) (R 5) (R 5) (R 2) (L 1) (L 3) (R 1) (R 4) (L 3) (R 1) (R 3) (L 5) (L 4) (R 2) (R 5) (R 2) (L 1) (L 5) (L 1) (L 1) (R 78) (L 3) (R 2) (L 3) (R 5) (L 2) (R 2) (R 4) (L 1) (L 4) (R 1) (R 185) (R 3) (L 4) (L 1) (L 1) (L 3) (R 4) (L 4) (L 1) (R 5) (L 5) (L 1) (R 5) (L 1) (R 2) (L 5) (L 2) (R 4) (R 3) (L 2) (R 3) (R 1) (L 3) (L 5) (L 4) (R 3) (L 2) (L 4) (L 5) (L 4) (R 1) (L 1) (R 5) (L 2) (R 4) (R 2) (R 3) (L 1) (L 1) (L 4) (L 3) (R 4) (L 3) (L 5) (R 2) (L 5) (L 1) (L 1) (R 2) (R 3) (L 5) (L 3) (L 2) (L 1) (L 4) (R 4) (R 4) (L 2) (R 3) (R 1) (L 2) (R 1) (L 2) (L 2) (R 3) (R 3) (L 1) (R 4) (L 5) (L 3) (R 4) (R 4) (R 1) (L 2) (L 5) (L 3) (R 1) (R 4) (L 2) (R 5) (R 4) (R 2) (L 5) (L 3) (R 4) (R 1) (L 1) (R 5) (L 3) (R 1) (R 5) (L 2) (R 1) (L 5) (L 2) (R 2) (L 2) (L 3) (R 3) (R 3) (R 1)))

(defparameter *initial-pos* '(N 0 0))

(defun distance (pos)
  (+ (cadr pos) (caddr pos)))

(defun move-pointing (cur turn)
  (cond ((equal cur 'N)
         (cond ((equal turn 'L) 'W)
               ((equal turn 'R) 'E)))
        ((equal cur 'S)
         (cond ((equal turn 'L) 'E)
               ((equal turn 'R) 'W)))
        ((equal cur 'W)
         (cond ((equal turn 'L) 'S)
               ((equal turn 'R) 'N)))
        ((equal cur 'E)
         (cond ((equal turn 'L) 'N)
               ((equal turn 'R) 'S)))))

(defun move-pos (dir steps pos)
  (cond ((equal dir 'N) (list (car pos) (+ (cadr pos) steps)))
        ((equal dir 'S) (list (car pos) (- (cadr pos) steps)))
        ((equal dir 'W) (list (- (car pos) steps) (cadr pos)))
        ((equal dir 'E) (list (+ (car pos) steps) (cadr pos)))))

(defun move (pos move)
  (let ((dir (move-pointing (car pos) (car move))))
        (cons dir (move-pos dir (cadr move) (cdr pos)))))

(defun compute-final (pos moves)
  (cond ((null moves) (distance pos))
        (t (compute-final (move pos (car moves)) (cdr moves)))))

(princ (compute-final *initial-pos* *input*))
