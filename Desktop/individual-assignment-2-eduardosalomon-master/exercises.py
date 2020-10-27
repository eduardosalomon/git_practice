
form = {
        "password": "password"
    }


def validate_form(form):
    if "email" not in form:
        raise KeyError("key \"email\" not present in form")
    if type(form["email"]) is not str:
        raise TypeError("email should be a string")
    if "@" not in form["email"] or "." not in form["email"]:
        raise ValueError("invalid email")

    return form

# ASSINGMENT 1
def handle_errors_validate_form(form):
    try:
        return validate_form(form)
    except KeyError:
            return("key not present in the form")
    except ValueError:
            return("there's something wrong about the values in your form")
    except TypeError:
            return("there's something wrong about the types in your form")

print(handle_errors_validate_form(form))
    


#%%
# ASSIGNMENT 2
def validate_user_score(score):
    if score != float:
        raise TypeError("score must be a float")
    if score < 5:
        raise ValueError("user failed: score too low")
    if score > 10:
        raise ValueError("user failed for cheating: score too high")
    return score





