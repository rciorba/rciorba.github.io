# wait for visibility
el =  WebDriverWait(self.parent, self.timeout).until(
    EC.presence_of_element_located(self._locator))
el = WebDriverWait(self.parent, self.parent.timeout).until(
    EC.visibility_of(el)
)

# wait for clickability
return WebDriverWait(self.parent, self.parent.timeout).until(
    EC.element_to_be_clickable(self._locator)
)
