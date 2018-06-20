
class MessagesHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        """Display all messages."""
        self.write('<a href="/compose">Compose a message</a><br>')
        self.write('<ul>')
        db = self.settings['db']
        db.messages.find().sort([('_id', -1)]).each(self._got_message)

    def _got_message(self, message, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        elif message:
            self.write('<li>%s</li>' % message['msg'])
        else:
            # Iteration complete
            self.write('</ul>')
            self.finish()
