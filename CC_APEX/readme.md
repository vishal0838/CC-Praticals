Executing this basic Apex code is the absolute first step in Salesforce development. Follow these exact steps to run it in your lab session:

---

## Step-by-Step Execution Guide

### **Step 1: Open the Developer Console**

1. Log in to your Salesforce account at [login.salesforce.com](https://login.salesforce.com/).
2. Look at the top right corner and click on the **Gear/Setup Icon**.
3. From the dropdown menu, click on **Developer Console**. A new workspace window will open up.

### **Step 2: Create and Save the Apex Class**

1. In the top-left menu of the Developer Console, click on **File** $\rightarrow$ **New** $\rightarrow$ **Apex Class**.
2. A popup will ask for the name. Enter exactly: `FirstClass1` and click **OK**.
3. Clear any default placeholder text and paste your code into the editor window:
```apex
public class FirstClass1
{
    public static void firstMethod()
    {
        System.debug('WELCOME TO PREC, Loni');
    }
}

```


4. Save the code by pressing **`Ctrl + S`** (or `Cmd + S` on Mac). Look at the bottom **"Problems"** tab to ensure there are no red syntax errors.

### **Step 3: Run (Execute) the Code**

1. In the top menu bar of the Developer Console, click on **Debug** $\rightarrow$ **Open Execute Anonymous Window**.
2. A separate code-entry popup window will appear.
3. Type the class name followed by the static method to call it:
```apex
FirstClass1.firstMethod();

```


4. Look at the bottom right corner of that popup and check the box that says **Open Log**.
5. Click the **Execute** button.

### **Step 4: View the Output**

1. The execution log file will open automatically on your screen.
2. At the bottom toolbar of the log viewer, check the filter box that says **Debug Only**.
3. The screen will filter out system noise, and you will clearly see your output line:
> `|USER_DEBUG|[5]|DEBUG|WELCOME TO PREC, Loni`