"""
    "1.กำหนดให้ brand_cars = (\"Toyota\", \"Honda\", \"Benz\", \"BMW\", \"Tesla\", \"Ford\", \"KIA\", \"Volvo\" )\n",
    "\n",
    "1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo\n",
    "1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล\n",
    "1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบมียี่ห้อรถ Suzuki, Ferrari, Ford อยู่ใน cars หรือไม่"

      "ตำแหน่งของ Benz คือ 2
      "ตำแหน่งของ Ford คือ 5
      "ตำแหน่งของ Volvo คือ 7
      "จำนวนข้อมูลทั้งหมดในทูเพิล คือ 8 รายการ
      "มียี่ห้อรถ Suzuki อยู่ใน brand_cars หรือไม่ = False
      "มียี่ห้อรถ Ferrari อยู่ใน brand_cars หรือไม่ = False\n",
      "มียี่ห้อรถ Ford อยู่ใน brand_cars หรือไม่ = True
      """
brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("Brand cars",brand_cars)
print("ตำแหน่งของ Benz คือ",brand_cars.index("Benz"))
print("ตำแหน่งของ Ford คือ",brand_cars.index("Ford"))
print("ตำแหน่งของ Volvo คือ",brand_cars.index("Volvo"))
print("จำนวนข้อมูลทั้งหมดในทูเพิล คือ",len(brand_cars),"รายการ")
print("มียี่ห้อรถ Suzuki อยู่ใน brand_cars หรือไม่ =","Suzuki" in brand_cars)
print("มียี่ห้อรถ Ferrari อยู่ใน brand_cars หรือไม่ =","Ferrari" in brand_cars)
print("มียี่ห้อรถ Ford อยู่ใน brand_cars หรือไม่ =","Ford" in brand_cars)