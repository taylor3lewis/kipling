#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import chardet
import re

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
user_agent += 'Chrome/23.0.1271.64 Safari/537.11'
mozilla5_0 = {'User-Agent': user_agent}


def strip_non_text(text):
    text = re.sub(r'[^a-zA-ZáàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ\s-]', '', text)
    text = re.sub(r'[^a-zA-ZáàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ\s-]', '', text)
    return text


def ascii_2_portuguese(text):
    text = text.decode('iso-8859-1')
    text = text.encode('latin1')
    return text


def get_html(page=None):
    """
    page: string with all HTML
    """
    if page is not None:
        try:
            request = urllib2.Request(page, headers=mozilla5_0)
            response = urllib2.urlopen(request)
            encoding = response.headers['content-type'].split('charset=')[-1]
            content_html = response.read()
            u_content = unicode(content_html, encoding).encode('utf-8')
            html_page = re.sub(ur'[^\p{Latin}]', u'', u_content, re.UNICODE)
            return html_page
        except Exception as error_generic:
            print str(error_generic) + " (trying something else...)"
            try:
                request = urllib2.Request(page, headers=mozilla5_0)
                response = urllib2.urlopen(request)
                content_html = response.read()
                result = chardet.detect(content_html)
                encoding = result['encoding']
                u_content = content_html.decode(encoding).encode('utf-8')
                html_page = re.sub(ur'[^\p{Latin}]', u'', u_content, re.UNICODE)
                return html_page
            except Exception as err:
                print str(err)
    else:
        print 'get_html(page="http://www.example.com")'


if '__main__' == __name__:
    content = get_html("http://www.ascii.cl/htmlcodes.htm")
    content = content.split("&#160;")[1]
    content = content.split("</table>")[0]
    # content = re.sub(r"[\t]", " ", content)
    content = content.replace("\r", "").replace("\n", "").replace("\t", "")
    content = re.findall(r"<TD align=\"center\">.+?</TD>", content)
    for line in content:
        sanitarized = line.replace("<br>", " ")
        sanitarized = re.sub(r"<.+?>", "", sanitarized)
        print sanitarized
