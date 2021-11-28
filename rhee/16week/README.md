## 최대공약수와 최소공배수
https://programmers.co.kr/learn/courses/30/lessons/12940

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. <br>
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.<br>
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.<br>

### 제한사항
- 두 수는 1이상 1000000이하의 자연수입니다.

### 입출력 예
|n|m|return|
|---|---|---|
|3|12|[3, 12]|
|2|5|[1, 10]|

<br>
입출력 예 설명<br>

**입출력 예 #1**<br>
위의 설명과 같습니다.<br><br>

**입출력 예 #2**<br>
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.<br><br>


---

## 소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/12921

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.

(1은 소수가 아닙니다.)

### 제한사항
- n은 2이상 1000000이하의 자연수입니다.

### 입출력 예
|n|result|
|---|---|
|10|4|
|5|3|
<br>
입출력 예 설명<br>

**입출력 예 #1** <br>
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
<br>

**입출력 예 #2** <br>
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환