from indictrans import Transliterator
r2i = Transliterator(source='eng', target='hin', rb=False, build_lookup=True)

eng = "himanshu mera naam hai"

hin = r2i.transform(eng, 1)

print(hin)

