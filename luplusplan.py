# ฟังก์ชันเช็คพาสเวิร์ด
def check_password():
    password = input('กรุณาใส่พาสเวิร์ด: ')
    if password == 'richrich08011991':
        return True
    else:
        print('พาสเวิร์ดไม่ถูกต้อง กรุณาลองใหม่')
        return False

# ฟังก์ชันหลักในการคำนวณต้นทุนเช่ารถ
def calculate_cost():
    # เลือกรถ
    print("\nเลือกรถ:")
    print("1. Alphard (25,000 JPY/Day)")
    print("2. รถตู้ (20,000 JPY/Day)")
    car_choice = input("เลือกหมายเลขรถ (1 หรือ 2): ")
    car_cost = 25000 if car_choice == '1' else 20000

    # จำนวนวันที่เช่า
    days = int(input("จำนวนวันที่เช่า: "))

    # เลือกออพชั่นเพิ่มเติม
    out_of_town = input("ออกต่างจังหวัด? (y/n): ").lower() == 'y'
    stay_overnight = input("ค้างคืนต่างจังหวัด? (y/n): ").lower() == 'y'
    interpreter = input("ใช้ล่าม / ไกด์? (y/n): ").lower() == 'y'
    interpreter_days = int(input("จำนวนวันที่ใช้ล่าม / ไกด์: ")) if interpreter else 0

    # คำนวณค่าใช้จ่าย
    fuel_cost = 5000 + (3000 if out_of_town else 0)
    parking_cost = 8000
    expressway_cost = 5000
    driver_cost = 20000
    overnight_cost = 20000 if stay_overnight else 0
    interpreter_cost = (20000 if stay_overnight else 16000) * interpreter_days

    # คำนวณต้นทุนรวม
    total_cost = days * (car_cost + fuel_cost + parking_cost + expressway_cost + driver_cost + overnight_cost) + interpreter_cost

    # แสดงผลลัพธ์
    print("\nต้นทุนรวมทั้งหมด (JPY):", total_cost)
    selling_price = (total_cost + (total_cost * 0.4)) * 0.23
    print("ราคาขาย (THB):", round(selling_price, 2))

# เรียกใช้ฟังก์ชัน
if check_password():
    calculate_cost()
