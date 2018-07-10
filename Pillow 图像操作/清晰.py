from PIL import Image, ImageEnhance

def ab(input_img, output_img, mat, factor):
    img = Image.open(input_img)
    enhancer = ImageEnhance.Brightness(img)
    out = enhancer.enhance(factor)    
    out_name = output_img + str(factor) + '.' + mat 
    

    out.save(out_name)
    print('输出名称:'+out_name)

ab('./img/q.jpg','./sc/scte_','jpg',1.3)