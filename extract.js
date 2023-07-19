function extractDomainName(url) {
    let parsedUrl = url.split("://").pop().split("/")[0];
    
    if (parsedUrl.startsWith("www.")) {
      parsedUrl = parsedUrl.substring(4);
    }
    
    if (parsedUrl.endsWith(".com")) {
      parsedUrl = parsedUrl.slice(0, -4);
    }
    
    return parsedUrl;
  }