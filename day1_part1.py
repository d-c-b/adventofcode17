with open('input_d1.txt', 'rU') as f:
  captcha = f.read()

captcha_count = 0

for i in range(len(captcha)):
    if captcha[i] == captcha[(i+1) % len(captcha)]:
      captcha_count += int(captcha[i])

print captcha_count
