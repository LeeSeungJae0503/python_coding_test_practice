def solution(rsp):
    mapping = {"2": "0", "0": "5", "5": "2"}
    return "".join(mapping[i] for i in rsp)