from pyscript import document, display # type: ignore

def calculate_gwa(event):
    # Get input values
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value

    subjects = ["Math", "Science", "English", "Filipino", "PE"]
    grades = []

    for subject in subjects:
        value = document.getElementById(subject).value
        if value:
            grades.append(float(value))

    if not grades:
        display("⚠️ Please enter your grades.", target="result")
        return

    gwa = sum(grades) / len(grades)

    # Determine remark
    if gwa >= 90:
        remark = "🎉 Excellent"
    elif gwa >= 85:
        remark = "😊 Very Good"
    elif gwa >= 80:
        remark = "👍 Good"
    elif gwa >= 75:
        remark = "🙂 Passed"
    else:
        remark = "💔 Failed"

    message = f"👩‍🎓 {firstname} {lastname}, your GWA is {gwa:.2f}.<br>{remark}"
    display(message, target="result")
