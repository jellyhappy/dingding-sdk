#!/usr/bin/python3
# @Time    : 2021-06-21
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


class WorkMessage(Core):

    def send_notification(self, msg, useridlist=None,  dept_id_list=None, to_all_user=False):
        """
        send work notification.

        :param agentid: agentid
        :param useridlist: user id list
        :param dept_id_list: id of departments
        :param to_all_user: whether send to all users.
        :param msg: json object.

        :return task_id: async task id.
        """
        url = f"{URL}/topapi/message/corpconversation/asyncsend_v2"
        data = {'agent_id': self._agentid,
                'msg': msg, 'dept_id_list': dept_id_list, 'useridlist': useridlist}
        res = self._post(url, data)
        return res['task_id']

    def update_status_bar(self, task_id, status_value, status_bg=None):
        """
        update status bar.

        :param task_id: task id
        :param status_value: status value, example: argeen.
        :param status_bg: background color of status bar.

        :return result: True
        """

        url = f"{URL}/topapi/message/corpconversation/status_bar/update"
        data = {'task_id': task_id,
                'status_value': status_value, 'status_bg': status_bg, 'agent_id': self._agentid}
        res = self._post(url, data)
        return True

    def get_notificatioin_progress(self, task_id):
        """
        get progress of notification.

        :param task_id: task id

        :return result: result of send. {'progress_in_percent': 100,'status':2} 0: not yet. 1: progressing 2. done
        """

        url = f"{URL}/topapi/message/corpconversation/getsendprogress"
        data = {'task_id': task_id, 'agent_id': self._agentid}
        res = self._post(url, data)
        return res['progress']

    def get_notification_result(self, task_id):
        """
        get result of notification.

        :param task_id: task id

        :return resutl: result of notification.
        """
        url = f"{URL}/topapi/message/corpconversation/getsendresult"
        data = {'task_id': task_id, 'agent_id': self._agentid}
        res = self._post(url, data)
        return res['send_result']

    def recall(self, task_id):
        """
        recall sent message.

        :param task_id: task id

        :return result: True
        """

        url = f"{URL}/topapi/message/corpconversation/recall"
        data = {'msg_task_id': task_id, 'agent_id': self._agentid}
        res = self._post(url, data)
        return True
