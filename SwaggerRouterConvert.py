import sublime, sublime_plugin

class SwaggerRouterConvertCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # Walk through each region in the selection
        for region in self.view.sel():
                selectedText = self.view.substr(region)
                convertedText = selectedText
                self.view.insert(edit, region.begin(),convertedText)

