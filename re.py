using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Data.Sql;
using System.Data.SqlClient;
using System.Data.OleDb;
using System.Windows.Forms;
using System.IO;
using System.Net.Mail;
using System.Net;
using System.Net.Mime;
using System.Web;
using System.IO.Compression;
using Microsoft.Win32;
using System.Net.Sockets;
using System.Runtime;


namespace TestDummyTWO
{
    public partial class Form1 : Form
    {
        FTPLib.FTP FTPLIB = new FTPLib.FTP();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            /* THIS IS THE FORMULA
             * TreeNode MyNodeMain = new TreeNode();
             * TreeNode MyNodeChild = new TreeNode();
             * MyNodeMain.Text = "Main";
             * MyNodeChild.Text = "child";
             
             * mytree.Nodes.Add(MyNodeMain);
             * MyNodeMain.Nodes.Add(MyNodeChild);
            */

           

            FTPLIB.server = "******";
            FTPLIB.user = "*******";
            FTPLIB.pass = "******";

            foreach (string S in FTPLIB.ListDirectories())
            {
                /*          Making parent node          */
                TreeNode ParentNode = new TreeNode();
                ParentNode.Text = S.Substring(55);
                treeView1.Nodes.Add(ParentNode);

                /*          Making child node           */

                FTPLIB.ChangeDir("//" + S.Substring(55) + "/");
                foreach (string S2 in FTPLIB.List())
                {
                    FTPLIB.ChangeDir("//" + S.Substring(55) + "/");

                    TreeNode ChildNode = new TreeNode();
                    ChildNode.Text = S2.Substring(55);
                    ParentNode.Nodes.Add(ChildNode);

                    FTPLIB.ChangeDir(".");
                }

            }
        }
    }
}