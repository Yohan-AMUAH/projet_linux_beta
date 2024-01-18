def processor(data):
    data['variation']=data["Adj Close"]/data["Adj Close"].shift(1) - 1
    data.dropna(inplace=True)
    annual_return =data["variation"].mean()*252
    standard_deviation= data["variation"].std()*100

    return (annual_return,standard_deviation)
