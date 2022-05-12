# Deepshikha
#CS21BTECH11016
# CBSE Probability Grade 12
#Exercise 13.1 11

S={1,2,3,4,5,6}
E={1,3,5}
F={2,3}
G={2,3,4,5}

X1=E.intersection(F)
X2=E.union(F)

Y1=E.intersection(G)
Y2=E.union(G)

Z1=X1.intersection(G)
Z2=X2.intersection(G)

s=len(S)
e=len(E)
f=len(F)
g=len(G)
x1=len(X1)
x2=len(X2)
y1=len(Y1)
y2=len(Y2)
z1=len(Z1)
z2=len(Z2)

#prob. of E
p_e=round(e/s,2)

#prob. of F
p_f=round(f/s,2)

#prob. of G
p_g=round(g/s,2)

#prob. of E intersection F
p_ef=round(x1/s,2)

#prob. of E union F
p_e_U_f=round(x2/s,2)

#prob. of E intersection G
p_eg=round(y1/s,2)

#prob. of E union G
p_e_U_g=round(y2/s,2)

#prob. of (E union F)intersection G
p_e_U_f_G=round(z2/s,2)

#prob. of (E intersection F) union G
p_e_inter_f_G=round(z1/s,2)

p_1=round(p_ef/p_f,1)
print("P(E|F):",p_1)

p_2=round(p_ef/p_e,2)
print("P(F|E):",p_2)

p_3=round(p_eg/p_g,1)
print("P(E|G):",p_3)

p_4=round(p_eg/p_e,2)
print("P(G|E):",p_4)

p_5=round(p_e_U_f_G/p_g,2)
print("P((EUF)|G):",p_5)

p_6=round(p_e_inter_f_G/p_g,2)
print("P((E inter F)|G):",p_6)
