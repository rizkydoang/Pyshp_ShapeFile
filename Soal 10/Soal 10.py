import shapefile
print(1194021 % 8)

w = shapefile.Writer("soal_10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("M. ", "RIZKY")
w.record("M. ", "RIZKY")

w.poly([[[5, 7], [8, 4], [5, 1], [2, 4]]])

w.poly([[[15, 7], [18, 4], [15, 1], [12, 4]]])


w.close()
