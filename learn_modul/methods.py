import db

def urunEkle(urunAdi,fiyat):
    db.urunler.append({
        'ad':urunAdi,
        'fiyat':fiyat,
        'id':len(db.urunler)+1 
        })
def urunGuncelle(id,urunAdi,fiyat):
    for urun in db.urunler:
        if(urun['id']==id):
            urun['ad']=urunAdi
            urun['fiyat']=fiyat
            break
def UrunGetir():
    for urun in db.urunler:
        print(f" id: {urun['id']} urun adi: {urun['ad']} fiyat: {urun['fiyat']} ")

