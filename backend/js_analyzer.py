import re
import requests
import openai

def fetch_js(target):
    response = requests.get(target)
    js_files = re.findall(r'src="(.*?\.js)"', response.text)
    return [target + js if js.startswith("/") else js for js in js_files]

def extract_sensitive_data(js_code):
    patterns = {
        "API Keys": r"(?i)(?:api[_-]?key|secret|token)['\"]?\s*[:=]\s*['\"]([A-Za-z0-9-_]+)['\"]",
        "Endpoints": r"https?://[^\s\"']+"
    }
    results = {key: re.findall(pattern, js_code) for key, pattern in patterns.items()}
    return results

def analyze_with_ai(js_code):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analyze this JavaScript code for security vulnerabilities:\n{js_code}"}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception:
        return "AI Analysis failed."

def analyze_target(target):
    js_files = fetch_js(target)
    full_analysis = {}

    for js_url in js_files:
        js_code = requests.get(js_url).text
        extracted_data = extract_sensitive_data(js_code)
        ai_analysis = analyze_with_ai(js_code)
        full_analysis[js_url] = {"extracted": extracted_data, "ai_analysis": ai_analysis}
    
    return full_analysis
