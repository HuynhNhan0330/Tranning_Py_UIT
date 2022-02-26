# Một số kiến thức cần thiết phục vụ cho phần còn lại của môn học

## Lũy thừa
$$
\begin{align*}
X^AX^B &= X^{A+B} \\
\frac{X^A}{X^B} &= X^{A-B} \\
(X^A)^B &= X^{AB} \\
X^N + X^N &= 2X^N \neq X^{2N} \\
2^N + 2^N &= 2^{N+1}
\end{align*}
$$

## Logarit
* Định nghĩa: $X^A$ = $B$ nếu và chỉ nếu $\log_X B=A$
* Định lý (lưu ý, nếu như không ghi cơ số thì mặc định là $2$ trong ngành công nghệ thông tin):

$$
\begin{align*}
\log_A B &= \frac{\log_C B}{\log_C A} \\
\log AB &= \log A + \log B; \quad A, B > 0 \\
\log A/B &= \log A - \log B \\
\log(A^B) &= B \log A \\
\log X &< X~\text{với mọi}~ X > 0 \\
\log 1 &= 0 \\
\log 2 &= 1 \\
\log 1,024 &= 10 \\
\log 1,048,576 &= 20
\end{align*}
$$

## Chuỗi
* Chuỗi hình học (hay chuỗi cấp số nhân):
$$
\begin{align*}
\sum_{i=0}^N 2^i &= 2^{N+1} - 1 \\
\sum_{i=0}^N A^i &= \frac{A^{N+1} - 1}{A - 1}~\text{với}~A \geq 1 \\
\sum_{i=0}^N A^i &\leq \frac{1}{1 - A}~\text{với}~ 0 \leq A \leq 1 
\end{align*}
$$

* Chuỗi số học cũng là một chuỗi phổ biến dùng để phân tích các thuật toán. Những chuỗi có dạng này đều có thể xấp xỉ để đơn giản trong việc phân tích.
$$
\begin{align*}
\sum_{i=1}^N i &= \frac{N(N+1)}{2} \approx \frac{N^2}{2} \\ 
\end{align*}
$$

## Số học mô đun


## Phương pháp quy nạp và phương pháp phản chứng


## Đệ quy


## Con trỏ
