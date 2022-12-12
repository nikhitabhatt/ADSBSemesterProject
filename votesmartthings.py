from votesmart import votesmart
votesmart.apikey = '9197774ffbb310adc3915516c2cf36f5'



for branch in votesmart.office.getBranches():
    print(branch)