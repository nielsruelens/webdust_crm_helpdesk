from openerp.osv import osv
from openerp.tools.translate import _
from email.message import Message
from openerp.addons.mail.mail_message import decode

class mail_thread(osv.AbstractModel):
    _name = "mail.thread"
    _inherit = "mail.thread"

    def message_parse(self, cr, uid, message, save_original=False, context=None):
        '''' parse reply-to and set author_id to reply-to partner '''
        result = super(mail_thread, self).message_parse(cr, uid, message, save_original, context)
        if not isinstance(message, Message):
            if isinstance(message, unicode):
                # Warning: message_from_string doesn't always work correctly on unicode,
                # we must use utf-8 strings here :-(
                message = message.encode('utf-8')
            message = email.message_from_string(message)
        result['reply-to'] = decode(message.get('Reply-To'))
        if message.get('Reply-To'):
            author_ids = self._message_find_partners(cr, uid, message, ['Reply-To'], context=context)
            if author_ids:
                result['author_id'] = author_ids[0]

        return result

