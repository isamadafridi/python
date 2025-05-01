'''5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 percent of
the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment
value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20.'''

#define the assessment value function
def assessment_value(actual_value):
    return actual_value * 0.6
    

def property_tax(assessment_value):
    return (assessment_value * 0.72) / 100


# Define the main function
def main():
    actual_value = float(input("Enter the actual value of the property:"))
    
    assessment = assessment_value(actual_value)
    print(f"The assessment value is: {assessment:.2f}")

    tax = property_tax(assessment)
    print(f"The total tax is: {tax:.2f}")

    

main()