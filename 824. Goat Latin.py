def toGoatLatin(S: str) -> str:
    S = list(S.split())
    result = []
    for count, x in enumerate(S):
        if x[0] in "aeiouAEIOU":
            result.append(x + "ma" + ("a" * (count + 1)))
        else:
            result.append(x[1:] + x[0] + "ma" + ("a" * (count + 1)))

    return ' '.join(result)


print(toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(toGoatLatin(
    "The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")

# Example 1:
#
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Example 2:
#
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
