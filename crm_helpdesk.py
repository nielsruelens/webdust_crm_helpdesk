from openerp.osv import osv
from openerp.tools.translate import _

class crm_helpdesk(osv.Model):
    _name = "crm.helpdesk"
    _inherit = "crm.helpdesk"

#    def message_post(self, cr, uid, thread_id, body='', subject=None, type='notification',
#                        subtype=None, parent_id=False, attachments=None, context=None,
#                        content_subtype='html', **kwargs):
#        ''' crm.helpdesk:message_post()
#            ---------------------------
#            This method overwrites the default behaviour to
#            make sure a closed case gets reopened if a new
#            message is posted.
#            ------------------------------------------------ '''
#
#        result = super(crm_helpdesk,self).message_post(cr, uid, thread_id, body, subject, type,
#                        subtype, parent_id, attachments, context, content_subtype, **kwargs)
#
#        for case in self.browse(cr, uid, [thread_id], context=context):
#            if case.state == 'done':
#                self.case_reset(cr, uid, [case.id], context=context)
#
#        return result

    def message_new(self, cr, uid, msg, custom_values=None, context=None):
        ''' replace email-from with reply-to if available, fallback on from (default) '''
        defaults = {}
        defaults['from'] = msg.get('reply-to') or msg.get('from')
        defaults['email_from'] = msg.get('reply-to') or msg.get('from')
        return super(crm_helpdesk, self).message_new(cr, uid, msg, custom_values=defaults, context=context)

