def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณหาราคาขายสินค้า --**')

def inputData( ) :
    product_name = input('ป้อนชื่อสินค้า : ')
    product_price = float( input( 'ป้อนราคาสินค้า(ต้นทุน) : '))
    return product_name, product_price

def calProductSale( product_price ) :
    product_sale = product_price + (product_price*10/100)
    return product_sale

def showProductSale( product_name, product_price, product_sale ) :
    print(f'ชื่อสินค้า {product_name}')
    print(f'ราคาสินค้า {product_price:.2f} บาท')
    print(f'ราคาขายสินค้า {product_sale:.2f} บาท')

showProgramName( ) 
print('--------------------------------------')
product_name, product_price = inputData( )
print('--------------------------------------')
product_sale = calProductSale( product_price )
print('--------------------------------------')
showProductSale( product_name, product_price, product_sale )
print('--------------------------------------')