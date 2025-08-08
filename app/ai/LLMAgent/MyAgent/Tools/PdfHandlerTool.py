from ..Tools.Tool import Tool
from ..utils.print_utils import log_tool_action
from pathlib import Path
import uuid
import os
from dotenv import load_dotenv

class PdfHandlerTool(Tool):

    def __init__(self, show_tool_call: bool =True):
       
       self._name = "Pdf_handling_tool"
       self._description = (
        "Creates and saves a PDF file.\n"
        "Arguments: Requires 'html_content' in valid HTML format and 'output_filename' as the desired output file name.\n"
        "Notes: When using <img> tags, always include both width and height attributes to ensure images fit correctly in the PDF.\n"
        "Supports basic inline CSS styling. External scripts and JavaScript are not supported."
        )

       
       self.show_tool_call = show_tool_call
       
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    def _run_implementation(self, html_content: str, output_filename: str):
        from weasyprint import HTML

        try:
            if self.show_tool_call:
                log_tool_action("Executing PDF Handling Tool", "...", "🗃️", "blue")
            
            load_dotenv()
            SERVER_URL_BASE = os.getenv("SERVER_URL_BASE")
            
            output_fileId = uuid.uuid4()
            path = Path(f'files/{output_fileId}.pdf')
            HTML(string=html_content).write_pdf(path)
            print(f"PDF saved successfully {path}")
            return {
                    "ok": True,
                    "pdf_id": uuid,
                    "filename": output_filename,
                    "download_url": f"{SERVER_URL_BASE}/files/download/{output_filename}.pdf/{output_fileId}"
                }

        except Exception as e:
            return {
                "ok": False,
                "message": f"Got error while creating/saving pdf {e}"
            }
        