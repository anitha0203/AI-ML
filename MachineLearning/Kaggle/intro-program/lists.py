# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
# avg_first_seven = sum(num_customer)
# avg_last_seven = ____ 
# max_month = ____
# min_month = ____

print(num_customers[-7:])



alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
print(alphabet.split('.'))
print(address.split(','))


# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    # growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago])/num_users[len(num_users)-2]
    print(num_users[len(num_users)-1])
    print(num_users[len(num_users) - yrs_ago -1])
    growth = (num_users[len(num_users)-1] - num_users[len(num_users) - yrs_ago-1]) / num_users[len(num_users) - yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))