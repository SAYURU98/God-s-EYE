# God-s-EYE
An intelligent phishing detector - Chrome extenmsion - using Machine learning

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>God's EYE Chrome Extension - Product Documentation</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 40px;
            background-color: #f9f9f9;
        }

        h1 {
            font-size: 32px;
            color: #1565c0;
            text-align: center;
            margin-bottom: 20px;
            text-decoration: underline;
        }

        h2 {
            font-size: 24px;
            color: #4caf50;
            margin-bottom: 10px;
        }

        p {
            font-size: 16px;
            color: #333;
            margin-bottom: 20px;
        }

        ul {
            margin-left: 30px;
        }

        li {
            font-size: 16px;
            color: #333;
            margin-bottom: 10px;
        }

        ol {
            margin-left: 30px;
            list-style-type: decimal;
        }

        code {
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
            color: #1565c0;
            background-color: #f1f1f1;
            padding: 3px 6px;
        }

        .cta-button {
            display: inline-block;
            background-color: #f44336;
            color: #fff;
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 10px;
        }

        .cta-button:hover {
            background-color: #e53935;
        }
    </style>
</head>

<body>
    <h1>God's EYE Chrome Extension - Product Documentation</h1>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">1. Introduction</a></li>
        <li><a href="#installation">2. Installation Guide</a></li>
        <li><a href="#usage">3. Usage Guide</a></li>
        <li><a href="#api">4. API Documentation</a></li>
        <li><a href="#model">5. Machine Learning Model</a></li>
        <li><a href="#dataset">6. Dataset</a></li>
        <li><a href="#conclusion">7. Conclusion</a></li>
    </ul>

    <h2 id="introduction">1. Introduction</h2>
    <p>
        God's EYE is a powerful Chrome Extension designed to detect and block phishing websites in real-time. It utilizes
        a machine learning model trained on a large dataset of URLs to accurately classify whether a given URL is
        malicious or benign. The extension works by sending the current URL of the user's active tab to a backend API,
        which processes the URL and returns a prediction. If the prediction indicates a high likelihood of the URL being
        a phishing site, the extension will block access to the site, protecting the user from potential threats.
    </p>

    <h2 id="installation">2. Installation Guide</h2>
    <p>
        To install God's EYE Chrome Extension, follow these steps:
    </p>
    <ol>
        <li>Visit the <a href="https://chrome.google.com/webstore/godseye" target="_blank">Chrome Web Store</a> page
            for God's EYE.</li>
        <li>Click on the "Add to Chrome" button.</li>
        <li>When prompted, review the permissions and click "Add extension" to complete the installation.</li>
    </ol>

    <h2 id="usage">3. Usage Guide</h2>
    <p>
        Using God's EYE Chrome Extension is simple:
    </p>
    <ol>
        <li>Browse the web as you normally would.</li>
        <li>If you navigate to a potentially malicious website, the extension will automatically block access and show
            you a warning message.</li>
        <li>Take caution when encountering blocked websites and avoid entering any personal information or login
            credentials.</li>
        <li>Report any false positives or false negatives to our support team for investigation.</li>
    </ol>

    <h2 id="api">4. API Documentation</h2>
    <p>
        The God's EYE API allows developers to integrate the phishing detection functionality into their own
        applications. Here are the details:
    </p>
    <ul>
        <li>Endpoint: <code>https://api.godseye.com/v1/check</code></li>
        <li>HTTP Method: POST</li>
        <li>Request Body: JSON object with a single property <code>url</code> representing the URL to check.</li>
        <li>Response: JSON object with a single property <code>prediction</code> indicating the predicted class of the
            URL (0 for benign, 1 for phishing).</li>
    </ul>

    <h2 id="model">5. Machine Learning Model</h2>
    <p>
        The machine learning model used by God's EYE Chrome Extension is a deep neural network trained on a large dataset
        of labeled URLs. The model leverages state-of-the-art natural language processing techniques to extract
        informative features from the URLs and make accurate predictions. Regular updates to the model ensure its
        effectiveness in detecting new and evolving phishing techniques.
    </p>

    <h2 id="dataset">6. Dataset</h2>
    <p>
        The training dataset used to train the machine learning model consists of millions of URLs labeled as either
        benign or phishing. The dataset is continuously updated and curated to ensure the highest quality and coverage
        of phishing websites.
    </p>

    <h2 id="conclusion">7. Conclusion</h2>
    <p>
        God's EYE Chrome Extension provides robust protection against phishing websites, safeguarding users from
        potential threats. By leveraging advanced machine learning techniques, the extension offers real-time detection
        and blocking capabilities. Install God's EYE today and browse the web with confidence!
    </p>

    <a class="cta-button" href="https://chrome.google.com/webstore/godseye" target="_blank">Get God's EYE Now!</a>
</body>

</html>

