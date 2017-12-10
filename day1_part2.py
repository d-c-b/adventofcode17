with open('input_d1.txt', 'rU') as f:
  captcha = f.read()

captcha_count = 0
half = len(captcha)/2

for i in range(len(captcha)):
    if captcha[i] == captcha[(i+half) % len(captcha)]:
      captcha_count += int(captcha[i])

print captcha_count
