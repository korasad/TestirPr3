def test():
  i=1
  while i<=3:
    if i == 1:
      testik = {1:"Лук", 2:"Топ-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5751500:
        print("test 1 выполнен")
    if i == 2:
      testik = {1:"Пистолет", 2:"Топ-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5751000:
        print("test 2 выполнен")
    if i == 3:
      testik = {1:"Пистолет", 2:"Тяп-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5750000:
        print("test 3 выполнен")
    i+=1