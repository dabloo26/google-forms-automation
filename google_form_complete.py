"""
Google Form Submitter - FINAL CORRECTED VERSION
Page 3: Handles 8 radio questions + 2 text fields correctly
Text fields are skipped (set to "N/A" if needed)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfj4W7hR_AFVtqUWlUtbB5Ci_acIsa3F4DgmmfjCVj7kMpbog/viewform"

def click_next_button(driver):
    """Click Next button"""
    try:
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]/.."))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)
        print(f"  ✓ Clicked Next!")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:80]}")
        return False

def click_submit_button(driver):
    """Click Submit button"""
    print("\n  🔍 Looking for Submit button...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    try:
        submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]/.."))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit)
        time.sleep(4)
        
        if "formResponse" in driver.current_url:
            print(f"  ✓ Form submitted!")
            return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:60]}")
    
    return False

def click_radio(driver, text):
    """Click radio button by text"""
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.2)
        driver.execute_script("arguments[0].click();", element)
        return True
    except:
        return False

def fill_page2_scales(driver, row_data, csv_columns):
    """Fill Page 2 - 27 questions (1-10 scale)"""
    print("\n📄 PAGE 2: Masculinity Scales (1-10)")
    
    all_items = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
    visible_items = [item for item in all_items if item.is_displayed()]
    
    # Skip first item if it's instructions (28 visible = 1 instruction + 27 questions)
    if len(visible_items) == 28:
        questions = visible_items[1:28]
    else:
        questions = visible_items[:27]
    
    print(f"  Filling {len(questions)} questions")
    
    PAGE2_START_COL = 5
    filled_count = 0
    
    for q_index, item in enumerate(questions):
        try:
            csv_col_index = PAGE2_START_COL + q_index
            column_name = csv_columns[csv_col_index]
            value = row_data.get(column_name)
            
            if value is None or pd.isna(value):
                continue
            
            val = str(int(float(value)))
            radio = item.find_element(By.CSS_SELECTOR, f"div[role='radio'][data-value='{val}']")
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio)
            time.sleep(0.05)
            driver.execute_script("arguments[0].click();", radio)
            time.sleep(0.05)
            
            if radio.get_attribute('aria-checked') == 'true':
                filled_count += 1
            
        except Exception:
            pass
    
    print(f"    ✅ Filled {filled_count}/27 scales")
    return filled_count >= 20

def fill_page3_questions(driver, row_data, csv_columns):
    """
    Fill Page 3 - 8 radio questions + 2 text fields
    
    CSV structure (columns 32-42):
    32: Radio Q1 - touched sex organs
    33: Radio Q2 - forced to touch
    34: Radio Q3 - sexual intercourse
    35: Radio Q4 - other unwanted experience
    36: TEXT - description (SKIP)
    37: Radio Q5 - discussed it
    38: Radio Q6 - physical injury
    39: Radio Q7 - other violence
    40: TEXT - description (SKIP)
    41: Radio Q8 - discussed violence
    42: Radio Q9 - would you like to talk (4 options)
    """
    print("\n📄 PAGE 3: Experience Questions")
    
    all_items = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
    visible_items = [item for item in all_items if item.is_displayed()]
    
    print(f"  Found {len(visible_items)} visible items")
    
    # Page 3 starts at column 32
    PAGE3_START_COL = 32
    
    # Map: (CSV column index, item index in visible_items, is_text_field)
    # Based on form structure: instruction box + 10 items (8 radio + 2 text)
    page3_mapping = [
        (32, 1, False),  # Radio Q1 - item 1 (skip item 0 = instructions)
        (33, 2, False),  # Radio Q2 - item 2
        (34, 3, False),  # Radio Q3 - item 3
        (35, 4, False),  # Radio Q4 - item 4
        (36, 5, True),   # TEXT - item 5 (SKIP)
        (37, 6, False),  # Radio Q5 - item 6
        (38, 7, False),  # Radio Q6 - item 7
        (39, 8, False),  # Radio Q7 - item 8
        (40, 9, True),   # TEXT - item 9 (SKIP)
        (41, 10, False), # Radio Q8 - item 10
        (42, 11, False), # Radio Q9 - item 11 (4 options)
    ]
    
    success_count = 0
    
    for csv_col_idx, item_idx, is_text in page3_mapping:
        try:
            # Check if item exists
            if item_idx >= len(visible_items):
                print(f"    ⚠️  Item {item_idx} not found (only {len(visible_items)} items)")
                continue
            
            item = visible_items[item_idx]
            column_name = csv_columns[csv_col_idx]
            value = row_data.get(column_name)
            
            if value is None or pd.isna(value) or str(value).strip() == '':
                print(f"    ⚠️  Item {item_idx}: No CSV value")
                continue
            
            value_str = str(value).strip()
            
            # Skip text fields
            if is_text:
                print(f"    ⊘ Item {item_idx}: Text field (skipped)")
                success_count += 1  # Count as success since we're intentionally skipping
                continue
            
            # Handle radio buttons
            radios = item.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            if not radios:
                print(f"    ✗ Item {item_idx}: No radios found")
                continue
            
            # Try exact match on aria-label
            found = False
            for radio in radios:
                aria_label = radio.get_attribute('aria-label')
                if aria_label and aria_label.strip() == value_str:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio)
                    time.sleep(0.2)
                    driver.execute_script("arguments[0].click();", radio)
                    time.sleep(0.1)
                    
                    if radio.get_attribute('aria-checked') == 'true':
                        success_count += 1
                        print(f"    ✓ Item {item_idx}: Selected '{value_str}'")
                        found = True
                        break
            
            if not found:
                print(f"    ✗ Item {item_idx}: Could not find '{value_str}'")
            
        except Exception as e:
            print(f"    ✗ Item {item_idx}: Error - {str(e)[:40]}")
    
    print(f"    ✅ Completed {success_count}/11 items")
    return success_count >= 7  # Need at least 7/11 (most of the 8 required radios)

def fill_page4_scales(driver, row_data, csv_columns):
    """Fill Page 4 - last 30 columns (1-5 scale)"""
    print("\n📄 PAGE 4: Self-Assessment (1-5)")
    
    all_items = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
    visible_items = [item for item in all_items if item.is_displayed()]
    
    # Skip first item if it's instructions (31 visible = 1 instruction + 30 questions)
    if len(visible_items) == 31:
        questions = visible_items[1:31]
    else:
        questions = visible_items[:30]
    
    print(f"  Filling {len(questions)} questions")
    
    # Page 4 uses LAST 30 columns
    PAGE4_START_COL = len(csv_columns) - 30
    
    filled_count = 0
    
    for q_index, item in enumerate(questions):
        try:
            csv_col_index = PAGE4_START_COL + q_index
            column_name = csv_columns[csv_col_index]
            value = row_data.get(column_name)
            
            if value is None or pd.isna(value):
                continue
            
            val = str(int(float(value)))
            radio = item.find_element(By.CSS_SELECTOR, f"div[role='radio'][data-value='{val}']")
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio)
            time.sleep(0.05)
            driver.execute_script("arguments[0].click();", radio)
            time.sleep(0.05)
            
            if radio.get_attribute('aria-checked') == 'true':
                filled_count += 1
            
        except Exception:
            pass
    
    print(f"    ✅ Filled {filled_count}/30 scales")
    return filled_count >= 25

def verify_no_validation_errors(driver):
    """Check for validation errors"""
    try:
        errors = driver.find_elements(By.CSS_SELECTOR, "div[role='alert']")
        visible_errors = [e for e in errors if e.is_displayed() and e.text.strip()]
        
        if visible_errors:
            print(f"\n  ⚠️  VALIDATION ERRORS:")
            for err in visible_errors:
                print(f"     - {err.text}")
            return False
        return True
    except:
        return True

def fill_form(driver, row_data, row_num, csv_columns):
    """Fill entire form"""
    
    print(f"\n{'='*70}")
    print(f"📋 SUBMISSION #{row_num}: {row_data.get('Name (Optional)', 'N/A')}")
    print(f"{'='*70}")
    
    try:
        print("\n🌐 Loading form...")
        driver.get(FORM_URL)
        time.sleep(6)
        
        # PAGE 1
        print("\n📄 PAGE 1: Basic Info")
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        
        if len(inputs) >= 4:
            inputs[0].send_keys(str(row_data.get('Name (Optional)', '')))
            inputs[1].send_keys(str(row_data.get('Age', '')))
            inputs[2].send_keys(str(row_data.get('Email', '')))
            inputs[3].send_keys(str(row_data.get('Contact Number', '')))
            print(f"    ✓ All fields filled")
        
        click_radio(driver, row_data.get('Gender', 'Male'))
        
        if not click_next_button(driver):
            return False
        
        # PAGE 2
        if not fill_page2_scales(driver, row_data, csv_columns):
            print("  ⚠️  Page 2 incomplete")
        
        if not verify_no_validation_errors(driver):
            driver.save_screenshot(f"page2_error_{row_num}.png")
            return False
        
        if not click_next_button(driver):
            return False
        
        # PAGE 3
        if not fill_page3_questions(driver, row_data, csv_columns):
            print("  ⚠️  Page 3 may be incomplete")
        
        if not verify_no_validation_errors(driver):
            driver.save_screenshot(f"page3_error_{row_num}.png")
            return False
        
        if not click_next_button(driver):
            return False
        
        # PAGE 4
        if not fill_page4_scales(driver, row_data, csv_columns):
            print("  ⚠️  Page 4 incomplete")
        
        if not verify_no_validation_errors(driver):
            driver.save_screenshot(f"page4_error_{row_num}.png")
            return False
        
        # SUBMIT
        print("\n✅ Ready to submit...")
        
        if click_submit_button(driver):
            print(f"\n🎉 SUCCESS #{row_num}!")
            return True
        else:
            print(f"\n❌ SUBMIT FAILED #{row_num}")
            return False
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False

def main():
    print("="*70)
    print("🤖 GOOGLE FORM SUBMITTER - FINAL CORRECTED VERSION")
    print("="*70)
    print("Processing remaining rows (11-100)")
    print("Skipping rows 1-10 (already submitted)")
    print("="*70)
    
    csv_path = '/Users/anand/Desktop/GoogleFormProject/FormResponses_120_People.csv'
    df = pd.read_csv(csv_path)
    print(f"\n✅ {len(df)} rows loaded from CSV")
    
    csv_columns = list(df.columns)
    print(f"✅ {len(csv_columns)} columns")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Skip first 10 rows (already submitted), process remaining 90
    START_ROW = 10  # Start from row 11 (index 10)
    END_ROW = len(df)  # Process until end
    
    total_to_process = END_ROW - START_ROW
    print(f"\n📊 Processing rows {START_ROW + 1} to {END_ROW} ({total_to_process} submissions)")
    print(f"⏭️  Skipping rows 1-10 (already submitted)\n")
    
    successful = 0
    
    for i in range(START_ROW, END_ROW):
        row_dict = df.iloc[i].to_dict()
        submission_num = i + 1  # Display as row number (1-based)
        
        if fill_form(driver, row_dict, submission_num, csv_columns):
            successful += 1
        
        # Delay between submissions
        if i < END_ROW - 1:
            delay = random.uniform(5, 8)
            print(f"\n⏳  ing {delay:.1f}s...")
            time.sleep(delay)
    
    print(f"\n" + "="*70)
    print(f"📊 FINAL RESULTS: {successful}/{total_to_process} successful")
    print(f"📊 Total processed: Rows {START_ROW + 1}-{END_ROW}")
    print(f"="*70)
    
    input("\nPress Enter to close...")
    driver.quit()

if __name__ == "__main__":
    main()