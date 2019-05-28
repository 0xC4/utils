from stopwatch import tic, toc
import improc as ip

tic()
x = ip.imread("/home/s2682192/Pictures/ZIPF_EN.png")
print(x.dtype)
b = ip.as_float_img(ip.binarize(x, 0.4))

c = ip.as_int_img(b)

# Show that both int and float images are the same
ip.timshow(b)
ip.timshow(c)

toc()
tic ("Blurring")
d = ip.blur(c, 20)
ip.timshow(d, 32)
toc()