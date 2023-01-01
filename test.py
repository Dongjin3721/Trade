import pyupbit

access = "AxsFGj3DGdysjJNxafxPnEcxpar9sgLmYxqz3Glx"          # 본인 값으로 변경
secret = "qH3TLERGS9HsKG9270wgWVD00bgkxEU9T8hU2Phw"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회